from LiteralChecker import NFA

## NFA for just decimal integers

states = {'q0','q1','q2','q3'}
alphabet = {'0','1','2','3','4','5','6','7','8','9','_'}
transitions = {
    'q0':{'0': {'q1'},}
}
start_state = 'q0'
accept_states = {'q1','q2'}

DecInt = NFA(states, alphabet, transitions, start_state, accept_states)
DecInt.addTransitionsMult('q0', [str(d) for d in range(1,10)],'q2')
DecInt.addTransitionsMult('q2', [str(d) for d in range(10)], 'q2')
DecInt.addTransitionsMult('q3', [str(d) for d in range(10)], 'q2')
DecInt.addTransitionsMult('q2', ['_'], 'q3')

##Testing

userInput = input()
print(DecInt.accepts(userInput))

# works perfectly
# DecInt.fileTest('in.txt', "out.txt")