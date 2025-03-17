import sys
import os
import pytest

#Includes use of ChatGPT to generate tests

# Add src/ to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulations import simulate_pipeline

def test_tobs_distribution():
    N, Rpred, Mpred, Vpred = 100, 0.75, 350, 10000
    Tobs_samples, _, _ = simulate_pipeline.run_simulation(N, Rpred, Mpred, Vpred, num_samples=1000)
    assert len(Tobs_samples) == 1000
    assert (Tobs_samples >= 0).all() and (Tobs_samples <= N).all()

