class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # {state: {symbol: {next_states}}}
        self.start_state = start_state
        self.accept_states = accept_states

    def _epsilon_closure(self, states):
        """Find the epsilon closure of a set of states."""
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            if '' in self.transitions.get(state, {}):  # Epsilon transition
                for next_state in self.transitions[state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def accepts(self, input_string):
        """Check if the NFA accepts the input string."""
        current_states = self._epsilon_closure({self.start_state})
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions.get(state, {}):
                    next_states.update(self.transitions[state][symbol])
            current_states = self._epsilon_closure(next_states)
        return bool(current_states & self.accept_states)



##Testing
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    'q0': {'a': {'q0', 'q1'}},
    'q1': {'b': {'q2'}},
    'q2': {}
}
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)
print(nfa.accepts("aab"))  # True
print(nfa.accepts("aba"))  # False
