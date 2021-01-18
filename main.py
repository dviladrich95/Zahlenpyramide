from sty import bg

def make_pyramid(basis):
    pyramid = []
    step = basis
    for i in range(len(basis)):
        pyramid.append(step)
        new_step = [step[i] + step[i + 1] for i in range(len(step) - 1)]
        step = new_step
    pyramid.reverse()
    return pyramid

def print_colors(pyramid,n=3):


    for i, step in enumerate(pyramid):
        line = ' ' * (len(pyramid)-i)
        for element in step:
            sign = element % n
            if sign:
                color = bg.black
            else:
                color = bg.white
            line = line + color + '  ' + bg.rs
        print(line)
    return

def print_pyramid(pyramid,n=2,width=6,numbers=True):
    colors_2=[bg.black,bg.white]
    colors_3=[bg.green,bg.yellow,bg.red]
    for i, step in enumerate(pyramid):
        line = ' ' * int((len(pyramid)-i)*width/2)
        for element in step:
            if element <=0:
                color= bg.da_grey
            else:
                sign = element % n
                if n==2:
                    color = colors_2[sign]
                elif n==3:
                    color = colors_3[sign]
            if numbers:
                line = line + color + str(element).center(width) + bg.rs
            else:
                line = line + color + ' '.center(width) + bg.rs
        print(line)
    return

basis_list=[[0]*(2**k)+[-1]+[0]*(2**k)+[10] for k in range(3)]
basis_left=[1]+sum(basis_list,[])+[1]
basis_left=[1,0,0,1,0,-1,0,1]
basis=basis_left+basis_left[::-1]



pyramid=make_pyramid(basis)

print_pyramid(pyramid)
