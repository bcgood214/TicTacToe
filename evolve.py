import random, helper
from agent import Agent
from opponent import Opponent

class Genetic:
    def __init__(self, geno_len, mrate, ex=6):
        self.gl = geno_len
        self.mrate = mrate
        self.ex = ex
    
    # generates a genotype
    def genind(self):
        # one binary string for each weight
        geno = []

        for i in range(self.gl):
            s = ""
            for j in range(self.ex):
                b = random.choice(['0', '1'])
                s += b
            geno.append(s)
        
        return geno
    
    # returns a genotype with a single bit flipped
    def mutate(self, geno):
        mutstr = random.randint(0, self.gl-1)
        mutind = random.randint(0, self.ex-1)

        geno_l = list(geno[mutstr])
        if geno_l[mutind] == '1':
            geno_l[mutind] = '0'
        else:
            geno_l[mutind] = '1'
        # print(geno_l)
        
        mutant = geno
        mutant[mutstr] = ""
        for ind in geno_l:
            mutant[mutstr] += ind
        return mutant

    def recombine(self, p1, p2):
        new_ind = []
        # print("Parents: {}; \n{}".format(p1, p2))
        for i in range(self.gl):
            base_str = p1[i]
            other_str = p2[i]
            if random.random() > 0.5:
                base_str = p2[i]
                other_str = p1[i]
            co_point = random.randint(1, self.ex-1)
            s = base_str[:co_point] + other_str[co_point:]

            new_ind.append(s)
        
        if self.mrate > random.random():
            # print("Mutation occurs")
            new_ind = self.mutate(new_ind)
        
        # print("Child: {}".format(new_ind))
        
        return new_ind

def decode(geno, ex):
    pheno = []
    # print(geno)
    for s in geno:
        # print(s)
        val = 0
        pos = ex
        for c in s:
            val += int(c)*(2**pos)
            pos -= 1
        pheno.append(val)
    return pheno

def play_game(agent, explore=True, show=False):
    initial_state = "n"*9
    board = helper.strtomat(initial_state)
    opp = Opponent()

    while True:
        opp.make_move(board)
        next_move = agent.move(board, explore)
        board = helper.strtomat(next_move)
        if helper.check_game(board):
            if helper.has_won(board, 'x'):
                return (True, board)
            else:
                return (False, board)


def eval_pool(pool):
    fitness = []
    for ind in pool:
        values = decode(ind, 5)
        a = Agent(weights=values)
        for i in range(200):
            play_game(a)
        trial_run = play_game(a, explore=False)
        print(trial_run)
        if trial_run[0]:
            print("Success")
            fitness.append((ind, 10))
        else:
            print("Failed")
            fitness.append((ind, 1))
        print(ind)
    return fitness

def rts(fp, size):
    pool = random.choices(fp, k=size)
    high_fitness = [ind[0] for ind in pool if ind[1] == 10]
    low_fitness = [ind[0] for ind in pool if ind[1] == 1]
    parents = []
    if len(high_fitness) < 2:
        if len(high_fitness) > 0:
            parents.append(high_fitness[0])
            parents.append(random.choice(low_fitness))
        else:
            parents = random.choices(low_fitness, k=2)
    elif len(high_fitness) > 2:
        parents = random.choices(high_fitness, k=2)
    else:
        parents = high_fitness
    
    return parents


def main(poolsize, gens, mutrate):
    g = Genetic(11, mutrate)
    pool = [g.genind() for i in range(poolsize)]
    
    for i in range(gens):
        fitness = eval_pool(pool)
        # weights = [elem[1] for elem in fitness]
        next_gen = []
        for j in range(poolsize):
            parents = rts(fitness, poolsize//4)
            child = g.recombine(parents[0], parents[1])
            next_gen.append(child)
        pool = next_gen
        print("End of generation {}".format(i))
    
    final = eval_pool(pool)
    return [elem[0] for elem in final if elem[1] == 10]




if __name__ == "__main__":
    # g = Genetic(11, 0.01)
    # p1 = g.genind()
    # print(p1)
    # print(g.mutate(p1))
    # p2 = g.genind()
    # pool = [p1, p2, g.genind(), g.genind(), g.genind(), g.genind()]
    # fp = eval_pool(pool)
    # for i in range(5):
    #     new = []
    #     fp = eval_pool(pool)
    #     for j in range(6):
    #         parents = rts(fp, 4)
    #         child = g.recombine(parents[0], parents[1])
    #         new.append(child)
    #     pool = new

    print(main(20, 10, 0.1))
