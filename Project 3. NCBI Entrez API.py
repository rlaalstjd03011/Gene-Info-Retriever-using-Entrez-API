# API(Application Programming Interface)
#: 서로 다른 프로그램끼리 소통하게 해주는 '중개인'또는 '창구' 같은 것

# NCBI를 매번 들어가서 직접 검색하는 대신 이걸로 바로 결과를 받아오기!
# Entrez는 NCBI가 만든 API라 이용 했을때 가져올 수 있다

from Bio import Entrez
Entrez.email = 'rlaalstjd03011@naver.com'

# 단일 유전자의 summary

handle = Entrez.esearch(db='gene',term= 'TP53[Gene Name] AND Homo sapiens[Organism]')
record = Entrez.read(handle)
handle.close()

print(record['IdList'])

# XML: 데이터를 구조화해서 저장하는 특별한 규칙을 가진 txt 파일! (Entrezgene_gene, Entrezgene_summary...etc)

handle = Entrez.efetch(db='gene',id='7157',retmode='xml') # efetch 함수: ID를 이용해서 자세한 정보를 가져온다!
record = Entrez.read(handle)
handle.close()

summary = record[0]["Entrezgene_summary"]
print(summary)

# 여러 유전자의 summary!

gene_names = ['TP53','BRCA1','EGFR']

def get_gene_summary(gene_name):
    handle = Entrez.esearch(db='gene',term = gene_name + ' [Gene Name] AND Homo sapiens[Organism]')
    record = Entrez.read(handle)
    handle.close()

    print(f'\n---{gene_name}에 대한 전체 레코드 ---')
    print(record)

    gene_ids = record.get("IdList")
    result_count = record.get("Count")

    print(f'\n---{gene_name} 에 대한 찾은 ID 목록: {gene_ids}')
    print(f'{gene_name}에 대한 검색된 결과 수: {result_count}')

    if gene_ids:
        print(f'{gene_name}에 대해 다음 유전자 ID를 찾았습니다: {', '.join(gene_ids)}')
        for gene_id in gene_ids:
            ncbi_gene_url = f'https://www.ncbi.nlm.nih.gov/gene/{gene_id}'
            print(f'{gene_name}의 NCBI Gene 페이지: {ncbi_gene_url}')
    else:
        print('유전자 ID를 찾지 못했습니다.')


for gene in gene_names:
    get_gene_summary(gene)

print('\n--- 모든 유전자 검색 완료 ---')










