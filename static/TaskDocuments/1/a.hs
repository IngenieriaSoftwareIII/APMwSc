{-# LANGUAGE DeriveFunctor #-}

import qualified Data.Functor as DF
import qualified Data.Sequence as DS
data Arbol a = Empty | Nodo  a (Arbol a) (Arbol a) deriving (Show, DF.Functor)



dfs :: Arbol a -> [a]
dfs tree = reverse $ dfs' tree []
    where 
        dfs' Empty  acc = acc
        dfs' (Nodo a h1 h2) acc = (dfs' h2 (dfs' h1 (a:acc)))

recorrido tree op = reverse $ bfs'  [] [tree]
    where 
        bfs' acc [] = acc
        bfs' acc (Empty:xs) = bfs' acc xs
        bfs' acc ((Nodo a h1 h2):xs) = bfs' (a:acc) newQueue
            where newQueue = ((op) xs [h1,h2])

bfs tree = reverse $ bfs'  [] [tree]
    where 
        bfs' acc [] = acc
        bfs' acc (Empty:xs) = bfs' acc xs
        bfs' acc ((Nodo a h1 h2):xs) = bfs' (a:acc) newQueue
            where newQueue = (xs) ++ [h1,h2]

buildTree :: Int -> a -> Arbol a
buildTree lvls t = returnB 0
	where 
        returnB x 
            = if x < lvls then 
                Nodo t (returnB (x+1)) (returnB (x+1)) 
            else 
                Nodo t Empty Empty

fillTreeDfs :: Arbol a -> Int -> Arbol Int
fillTreeDfs tree n = fill tree n
    where 
        fill (Nodo a Empty Empty) n =  (Nodo n Empty Empty)
        fill (Nodo a t1 t2) n = Nodo n (fill t1 (n+1)) (fill t1 (n+1))

splitInTwo :: [a] -> ([a],[a])
splitInTwo (x:[]) = ([x], [])
splitInTwo list = splitAt ((length list) `div` 2) list


-- fromListToTree :: [a] -> Arbol a
fromListToTree []   = Empty
fromListToTree list = Nodo (head list) (fromListToTree (fst split)) (fromListToTree (snd split))
    where split = splitInTwo $ tail list
    


    

