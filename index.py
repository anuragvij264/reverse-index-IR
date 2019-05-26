from collections import Counter

class Index(object):
    def __init__(self,doc_tokens):
        """
        Expecting a list of list (documents as list of tokens)

        """
        docids = list()
        self.docs = dict()
        for docid,tokens in enumerate(doc_tokens):
            docids.append(docid)
            self.docs[docid] = tokens

        self.counts_dictionary = self.create_count_dict(self.docs)
        self.index  = self.create_index(self.docs,self.counts_dictionary)

    def gentoken2idx(docs):
        idx2token = dict()
        tokenList  = list()
        for doc in docs:
            for token in doc:
                tokenList.append(token)
        for idx,token in enumerate(tokenList):
            idx2token[idx] = token
        return token2idx

    def create_index(self,docs,count_dict):
        """

        docs == a dictionary of docs
        """
        index = {}
        for docid in docs.keys():
            doc = docs[docid]
            for token in doc:
                # if token in index.keys():
                #     temp_list.append(docid)
                temp_list = [[docid,self.get_counts(docid,token,count_dict)]]
                if token not in index.keys():
                    index[token]= temp_list
                else: index[token].append([docid,self.get_counts(docid,token,count_dict)])
                temp_list = []
        return index

    def create_count_dict(self,docs):
        count_dict = dict()
        for docid in self.docs.keys():
            count_dict[docid]=dict(Counter(self.docs[docid]))
        return count_dict

    def get_counts(self,docid,token,count_dict):
        """
        {'docid':{'token':c1,'token2':c2,...}}
        """
        return count_dict[docid][token]

    def update_count_dict(self,count_dict,document):
        docid = document[docid]
        new_count_dict = count_dict.update({docid:dict(Counter(document))})
        return new_count_dict

    def update_index(self,document):
        new_count_dict = self.update_count_dict(self.count_dict,document)
        new_index = self.create_index(self.docs.append(document),new_count_dict)
        return new_index

    def get_index(self):
        return self.index


if __name__=='__main__':
    """

    """

    object_1 =  Index(doc_tokens=[['I','am','happy']])
    print(object_1.get_index())
