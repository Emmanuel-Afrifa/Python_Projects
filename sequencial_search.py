def searcher(seq, num):
    for i,ele in enumerate(seq):
        if ele == num:
            print(f"Found {num} at index {i}")
            return True
            
if __name__ == "__main__":
    seq = [1,1,2,3,5,8,13,21]
    searcher(seq,13)

