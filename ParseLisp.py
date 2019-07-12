import collections
def evaluate(expression):
    def tokenizer(expression):
        return collections.deque(expression.replace('(', '( ').replace(')', ' )').split(' '))

    def eval(env, tokens):
        if tokens[0] != '(':
            token = tokens.popleft()
            if token[0] in '0123456789-':
                return int(token)
            else:
                return env[token]

        else:
            tokens.popleft()
            if tokens[0] in ('add', 'multi'):
                op = tokens.popleft()
                left, right = eval(env, tokens), eval(env, tokens)
                val = left+right if op == 'add' else left*right
            else:
                #let
                tokens.popleft()
                local = env.copy()
                while tokens[0] != '(' and tokens[1] != ')':
                    name= tokens.popleft()
                    local[name] = eval(local, tokens)
                val = env(local, tokens)
            tokens.popleft()
            return val
    return eval({}, tokenizer(expression))