import time
import sys
from loguru import logger
from chaos_ingestor import ChaosIngestor
from entropy_engine import EntropyEngine
from kinetic_driver import KineticDriver

def run_entropy_loop():
    logger.remove()
    logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>")
    
    logger.info("=== INITIALIZING ENTROPY CLOCK ===")
    
    ingestor = ChaosIngestor()
    engine = EntropyEngine()
    driver = KineticDriver()
    
    logger.warning("TIME DECONSTRUCTION COMMENCING. Linear time is now irrelevant.")
    
    try:
        while True:
            # 1. Sample the world's chaos
            samples = ingestor.get_latest_entropy_samples()
            
            # 2. Calculate the entropic shift
            vector = engine.calculate_chaos_vector(samples)
            
            # 3. Physically actuate the entropy
            driver.execute_movement(vector)
            
            # Wait for the next ripple in reality
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.error("Linear reality restored. System shutdown.")

if __name__ == "__main__":
    run_entropy_loop()
