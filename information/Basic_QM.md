# Description Of Different Gates

* In QM we represent our qubit states as vectors, we can consider quantum gates as matrices that can transform the vectors.
* Gates can be considered as operations on qubits that change their state from one to another.
* Any normalized pure state can be written in the following form:
 ```math
 |q> \ = \cos(\frac{\theta}{2})|0> \ + \ \ e^{i\phi} \sin(\frac{\theta}{2})|1>
 ```
* ` θ ∈ [0,π] ` determines the probability that the measurement results in `|0⟩` or `|1⟩`.
* The states `|0⟩` and `|1⟩` are often used as the basis states for representing all other quantum states, just as `0` and `1` are used as the basis states for representing all classical bit strings. 


## Basic States `|0>` and `|1>`

1. The state `|0⟩` represents the qubit in the **_"ground state"_** or **_"zero state"_**.

    - It is a superposition of all possible states that have *zero amplitude*, except for the state where the coefficient of the `|0⟩` state is `1` and all other coefficients are `0`. 
    - In other words, the state `|0⟩` has `100%` probability of being measured in the `|0⟩` state.


2. The state |1⟩, on the other hand, represents the qubit in the **_"excited state"_** or **_"one state"_**. 
    - It is a superposition of all possible states that have *zero amplitude*, except for the state where the coefficient of the `|1⟩` state is `1` and all other coefficients are `0`.
    - In other words, the state `|1⟩` has `100%` probability of being measured in the `|1⟩` state.


## X Gate (NOT Gate)

1. The `X` gate, also known as the `NOT` gate, is a quantum logic gate that acts on a *single qubit*. 
2. It is one of the most fundamental gates in quantum computing and is used in many quantum algorithms and circuits.
3. The `X` gate is represented by the *Pauli-X matrix*, which is a `2x2` matrix that flips the amplitudes of the `|0⟩` and `|1⟩` states.
4. When applied to a qubit in the state `|0⟩`, the `X` gate transforms it to the state `|1⟩`, and when applied to a qubit in the state `|1⟩`, it transforms it to the state `|0⟩`.
5. Mathematically, the action of the `X` gate can be represented as follows:
```math
X|0> \ = \ \ |1>
```
```math
X|1> \ = \ \ |0>
```
where,
```math
X = \left\lbrack \matrix{0 & 1 \cr 1 & 0} \right\rbrack = |0><1| \ + \ |1><0|
```
6. In other words, the X gate performs a bit-flip operation on a qubit, changing the state from `|0⟩` to `|1⟩` or vice versa. 
7. The `X` gate is a *crucial* building block for quantum circuits and is often used in combination with other gates to implement complex quantum algorithms.


