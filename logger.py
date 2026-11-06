import logging

logging.basicConfig(
    filename="frightfinder.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("frightfinder")