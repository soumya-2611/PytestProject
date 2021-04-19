import logging


class Loggen:

    @staticmethod
    def loggen():
        #logging.basicConfig(filename=".\\logsfolder\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I%M%S %p')

        logging.basicConfig(filename="C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\logsfolder\\automation.log",
                            format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',force=True)

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

