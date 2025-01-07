from loguru import logger

logger.debug("Um aviso para o desenvolvedor (ou eu mesmo ) no futuro")
logger.info("Informacao importante de processo")
logger.warning("Um aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma falha que aborta a aplicacao")