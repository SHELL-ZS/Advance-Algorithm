y = "ABBCCD"
c = []
for i in range(0,len(y),2):
    c.append(y[i])
print(c + str(sorted(list(set(y)))))

'''
{
(1, 1): [[4.5, 4.5], ['ACCBBD', 'ACCBBD']], 
(1, 4): [[5, 3.5], ['ACCD', 'ACCBBD']], 
(1, 6): [[6.5, 2.5], ['ABBCCD', 'ACCBBD']], 
(3, 4): [[4, 5.0], ['ACCD', 'ABBCCBBD']], 
(4, 1): [[3.5, 5], ['ACCBBD', 'ACCD']], 
(4, 3): [[5.0, 4], ['ABBCCBBD', 'ACCD']], 
(4, 4): [[5, 5], ['ACCD', 'ACCD']], 
(4, 6): [[6.5, 4], ['ABBCCD', 'ACCD']], 
(6, 1): [[2.5, 6.5], ['ACCBBD', 'ABBCCD']], 
(6, 4): [[4, 6.5], ['ACCD', 'ABBCCD']], 
(6, 6): [[6.5, 6.5], ['ABBCCD', 'ABBCCD']]}


                                                          player1 (i)
               (ci,cj)    'ABBD'   'ACCBBD'   'ABBAACCBBD'   'ABBCCBBD'   'ACCD'   'ABBAACCD'   'ABBCCD'
           'ABBD'      [[[5, 5]  , [3.5, 5]   , [9.5, 5]    , [6.0, 5]  , [4, 4]  , [10, 4]  , [6.5, 4]], 
           'ACCBBD'     [[5, 3.5], [4.5, 4.5] , [10.5, 4.5] , [6.0, 3.5], [5, 3.5], [11, 3.5], [6.5, 2.5]], 
           'ABBAACCBBD' [[5, 9.5], [4.5, 10.5], [10.5, 10.5], [6.0, 9.5], [5, 9.5], [11, 9.5], [6.5, 8.5]], 
player2(j) 'ABBCCBBD'   [[5, 6.0], [3.5, 6.0] , [9.5, 6.0]  , [6.0, 6.0], [4, 5.0], [10, 5.0], [6.5, 5.0]], 
           'ACCD'       [[4, 4]  , [3.5, 5]   , [9.5, 5]    , [5.0, 4]  , [5, 5]  , [11, 5]  , [6.5, 4]], 
           'ABBAACCD'   [[4, 10] , [3.5, 11]  , [9.5, 11]   , [5.0, 10] , [5, 11] , [11, 11] , [6.5, 10]], 
           'ABBCCD'     [[4, 6.5], [2.5, 6.5] , [8.5, 6.5]  , [5.0, 6.5], [4, 6.5], [10, 6.5], [6.5, 6.5]]] 


                           player1 (i)
           (ci,cj)   'ABBD'    'ACCD'     'ABBCCD'
           'ABBD'  [[[5, 5]  , [4, 4]  , [6.5, 4]], 
player2(j) 'ACCD'   [[4, 4]  , [5, 5]  , [6.5, 4]], 
           'ABBCCD' [[4, 6.5], [4, 6.5], [6.5, 6.5]]]


                          player1 (i)
           (ci,cj)  'ABBD'    'ACCBBD'    'ACCD'
           'ABBD' [[[5, 5]  , [3.5, 5]  , [4, 4]], 
player2(j) 'ACCBBD'[[5, 3.5], [4.5, 4.5], [5, 3.5]], 
           'ACCD'  [[4, 4]  , [3.5, 5]  , [5, 5]]]



                        player1 (i)
player3(h)         (ci,cj,ch)  'ABBD'     'ACCD'
'ABBD'   player2(j) 'ABBD' [[[[6, 6, 6], [4, 5, 5]], 
                    'ACCD'   [[5, 4, 5], [5, 5, 4]]], 

                        player1 (i)
player3(h)         (ci,cj,ch)  'ABBD'     'ACCD'
'ACCD'    player2(j) 'ABBD'  [[[5, 5, 4], [5, 4, 5]], 
                     'ACCD'   [[4, 5, 5], [6, 6, 6]]]]


'''