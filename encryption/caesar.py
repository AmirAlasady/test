
class Caeser():
    vocab={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
            6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
              12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
                18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
                  24: 'y', 25: 'z', 26: ' '}
    
    def __init__(self,key: int) -> None:
        self.key=key
        
    def view_vocab(self):
        print(self.vocab)

    def encrypet(self,text:str):
        text=text.lower()
        # shift + store
        off_let_num=[]
        for i in iter(text):
            for k,v in self.vocab.items():
                if i == v:
                    off_let_num.append((k+self.key) %27)
                    break
        # resolve to new letters
        encrypted_text=''
        for j in off_let_num:
            for k2, v2 in self.vocab.items():
                if j==k2:
                    num_to_let=self.vocab[k2]
                    encrypted_text=encrypted_text+num_to_let
                    break
        return encrypted_text
    
    def decrypt(self,text):
        # unshift + store
        un_off_let_num=[]
        for i in iter(text):
            for k,v in self.vocab.items():
                if i == v:
                    un_off_let_num.append((k-self.key) %27)
                    break
        # resolve to new letters
        decrypted_text=''
        for j in un_off_let_num:
            for k2, v2 in self.vocab.items():
                if j==k2:
                    num_to_let=self.vocab[k2]
                    decrypted_text=decrypted_text+num_to_let
                    break
        return decrypted_text            

