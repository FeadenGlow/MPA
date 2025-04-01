import json
import os

class MealyMachine:
    def __init__(self, states, input_alphabet, transitions, initial_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.history = []
    
    def process_input(self, input_string):
        output_string = ""
        for symbol in input_string:
            if (self.current_state, symbol) in self.transitions:
                next_state, output = self.transitions[(self.current_state, symbol)]
                self.history.append([self.current_state, symbol, output])
                self.current_state = next_state
                output_string += output
            else:
                raise ValueError(f"Invalid transition from {self.current_state} with input {symbol}")
        return output_string
    
    def display_transitions(self):
        print("State Transition Table:")
        for (state, symbol), (next_state, output) in self.transitions.items():
            print(f"{state} --({symbol}/{output})--> {next_state}")
    
    def save_to_json(self, filename="Mealy.json"):
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        data = {
            "current_state": self.current_state,
            "history": self.history
        }
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_from_json(self, filename="Mealy.json"):
        input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        with open(input_path, "r") as f:
            data = json.load(f)
            self.current_state = data["current_state"]
            self.history = data["history"]

    def convert_to_moore(self):
        moore_states = {}
        moore_transitions = {}
        state_counter = 0

        for (state, symbol), (next_state, output) in self.transitions.items():
            if state not in moore_states:
                moore_states[state] = f"M{state_counter}"
                state_counter += 1
            if next_state not in moore_states:
                moore_states[next_state] = f"M{state_counter}"
                state_counter += 1
            moore_transitions[(moore_states[state], symbol)] = moore_states[next_state]
        
        moore_initial_state = moore_states[self.current_state]
        moore_output_map = {moore_states[state]: output for (state, _), (_, output) in self.transitions.items()}
        
        return MooreMachine(set(moore_states.values()), self.input_alphabet, moore_transitions, moore_initial_state, moore_output_map)

class MooreMachine:
    def __init__(self, states, input_alphabet, transitions, initial_state, output_map):
        self.states = states
        self.input_alphabet = input_alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.output_map = output_map
    
    def process_input(self, input_string):
        output_string = self.output_map.get(self.current_state, "")
        for symbol in input_string:
            if (self.current_state, symbol) in self.transitions:
                self.current_state = self.transitions[(self.current_state, symbol)]
                output_string += self.output_map.get(self.current_state, "")
            else:
                raise ValueError(f"Invalid transition from {self.current_state} with input {symbol}")
        return output_string

if __name__ == "__main__":
    states = {"S0", "S1"}
    input_alphabet = {"a", "b"}
    transitions = {
        ("S0", "a"): ("S1", "0"),
        ("S0", "b"): ("S0", "0"),
        ("S1", "a"): ("S1", "0"),
        ("S1", "b"): ("S0", "1"),
    }
    initial_state = "S0"

    mealy = MealyMachine(states, input_alphabet, transitions, initial_state)
    mealy.display_transitions()
    input_string = "aabb"
    output_string = mealy.process_input(input_string)
    print(f"Input: {input_string} -> Output: {output_string}")
    mealy.save_to_json()
    
    moore = mealy.convert_to_moore()
    moore_output = moore.process_input(input_string)
    print(f"Moore Output: {moore_output}")

