import re
import logging
from dataclasses import dataclass
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Product:
    """
    Immutable data model representing a Product.
    Using a dataclass ensures type safety and clear structure.
    """
    product_id: str
    name: str
    price: float
    is_in_stock: bool


class HTMLDataExtractor:
    """
    A high-performance extractor for structured HTML data.
    Uses pre-compiled Regex for efficiency in high-throughput environments.
    """
    ITEM_PATTERN = re.compile(
        r'<div class="item" id="(?P<id>\d+)">'
        r'.*?<h2.*?class="name">(?P<name>.*?)</h2>'
        r'.*?class="price">\$(?P<price>.*?)</span>'
        r'.*?class="status">(?P<status>.*?)</p>',
        re.DOTALL
    )

    @staticmethod
    def _clean_price(price_str: str) -> float:
        """Helper to sanitize and convert price strings."""
        try:
            return float(price_str.replace(",", ""))
        except ValueError:
            return 0.0

    def extract_products(self, html_content: str) -> List[Product]:
        """
        Parses HTML and returns a list of validated Product objects.

        :param html_content: The raw HTML string to parse.
        :return: A list of Product dataclasses.
        """
        products = []

        matches = self.ITEM_PATTERN.finditer(html_content)

        for match in matches:
            try:
                raw_data = match.groupdict()

                new_product = Product(
                    product_id=raw_data['id'],
                    name=raw_data['name'].strip(),
                    price=self._clean_price(raw_data['price']),
                    is_in_stock="In Stock" in raw_data['status']
                )
                products.append(new_product)

            except Exception as e:
                logger.error(f"Error parsing product block: {e}")
                continue

        logger.info(f"Successfully extracted {len(products)} products.")
        return products


if __name__ == "__main__":
    mock_html = """
    <div class="product-list">
        <div class="item" id="101">
            <h2 class="name">Wireless Mouse</h2>
            <span class="price">$25.99</span>
            <p class="status">In Stock</p>
        </div>
        <div class="item" id="102">
            <h2 class="name">Mechanical Keyboard</h2>
            <span class="price">$85.00</span>
            <p class="status">Out of Stock</p>
        </div>
    </div>
    """

    extractor = HTMLDataExtractor()
    results = extractor.extract_products(mock_html)

    for item in results:
        print(item)