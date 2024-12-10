# 1. read input 
# 2. graph representation?
# 3. look for trailheads 0
# 4. iterate through input, do a bfs at each trailhead 

"""Tirakirja: leveyshaku taulukossa
procedure haku(y,x)
    if y < 0 or x < 0 or y >= n or x >= n
        return
    if seina[y][x] or vierailtu[y][x]
        return
    vierailtu[y][x] = true
    
    haku(y+1,x)
    haku(y-1,x)
    haku(y,x+1)
    haku(y,x-1)

    + voi siirtyä naapuriin vain jos arvo on solmu + 1
    + laske montako reittiä on eli counter += 1 aina kun pääseen ysiin
"""