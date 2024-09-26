import logging

logging.basicConfig(
    level=logging.ERROR, 
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 

