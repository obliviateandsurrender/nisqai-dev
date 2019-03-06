#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from nisqai.encode._wavefunction_encoding import WavefunctionEncoding, make_program

from numpy import array, linalg, matmul, random # functions yousif used
from pyquil.api import WavefunctionSimulator

def input_output_comparison_test():
    n = random.randint(4,8)
    x = random.normal(size=2**n) + 1j*random.normal(size=2**n)
    x = x / linalg.norm(x)
    U = WavefunctionEncoding(x)   
    e_0 = [0]*(2**n)
    e_0[0] = 1
    out = matmul(U,array(e_0).T)
    """
    print("U",U)
    print("UU*", matmul(U,U.conj().T))
    print("U*U", matmul(U.conj().T,U))
    print("x",x)
    print("out", out)
    print(abs(linalg.norm(x - out)))
    """
    # Check 2-norm distance between desired state and 
    # the state that the created unitary maps |00...0> t0.
    assert linalg.norm(x - out) < 1e-3

def test_program():
    n = random.randint(4,8)
    x = random.normal(size=2**n) + 1j*random.normal(size=2**n)
    x = x / linalg.norm(x)
    U = WavefunctionEncoding(x) 
    wf_sim = WavefunctionSimulator()
    p = make_program(U)
    wf = wf_sim.wavefunction(p)
    print(wf)

if __name__ == "__main__":
    input_output_comparison_test()
    test_program()
    print("All tests for WavefunctionEncoding passed.")