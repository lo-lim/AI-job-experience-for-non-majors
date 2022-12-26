import re
sentence = "제주도 숙소 추천해줘."
endings = ["알려줘.", "추천해줄래?", "알려줄래?", "추천좀", "추천"]
outputs = [re.sub("\w+\.$", x, sentence) for x in endings]
print(outputs)

import re
sentence = "제주도 숙소 어디가 좋을까?"
endings = ["좋아?", "좋니?", "괜찮아?", "괜찮을까?", "예뻐?", "예쁠까?"]
outputs = [re.sub("\w+\.$", x, sentence) for x in endings]
print(outputs)

import re
sentence = "어느 제주도 숙소가 좋을까?"
endings = ["좋아?", "좋니?", "괜찮아?", "괜찮을까?", "예뻐?", "예쁠까?"]
outputs = [re.sub("\w+\.$", x, sentence) for x in endings]
print(outputs)

import random
sentence = "나 제주도 숙소 좀 추천해줘."
fillers = ["음", "뭐지", "그", "흠", "어", "저"]
split_sent = sentence.split()
outputs = []
for idx in range(len(split_sent)):
     new_sent = split_sent[:]
     filler = random.choice(fillers)
     new_sent.insert(idx, filler)
     print(" ".join(new_sent))

sentence = "제주도 숙소 추천해줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "어느 숙소가 좋아?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주 숙소 추천"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "숙소는 어디가 좋아?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "괜찮은 제주도 숙소 어디야?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주 숙소 예쁜 곳 추천해 줘"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 좋을까?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 좋아?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 좋니?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 괜찮니?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 괜찮아?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 예쁜 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 괜찮은 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 편안한 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 마당 있는 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 감성 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 갈만한 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 분위기 좋은 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 가족끼리 갈만한 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 오션뷰 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 바다 보이는 숙소 알려줘."
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 어디가 예뻐?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 예쁜 숙소 어디에 있어?"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 예쁜 숙소 추천"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주도 숙소 괜찮은 곳 추천해 줘"
accomodation = ["호텔", "잘 곳", "게스트하우스", "독채", "독채숙소", "펜션", "오션뷰", "풀빌라", "모텔", "머무를 곳"]
outputs = [re.sub("숙소", x, sentence) for x in accomodation]
print(outputs)

sentence = "제주 숙소 예쁜 곳 추천해 줘"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 숙소 추천해 줘."
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "예쁜 제주도 숙소는 어디야?"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 숙소 추천"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 숙소 알려줘.]"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 펜션 알려줘.]"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 독채 알려줘.]"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 풀빌라 알려줘.]"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주 예쁜 게스트하우스 알려줘.]"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 숙소 어디에 있어?"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 호텔 어디에 있어?"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 호텔 추천"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 호텔 추천해 줘."
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 독채펜션 추천해 줘."
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 독채펜션"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 펜션 추천"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 독채"
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 풀빌라 추천해 줘."
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 예쁜 오션뷰 호텔 추천해 줘."
pretty = ["분위기 좋은", "편안한", "마당 있는", "가족끼리 갈만한", "괜찮은", "감성", "오션뷰", "바다뷰", "바다 보이는", "한달살기"]
outputs = [re.sub("예쁜", x, sentence) for x in pretty]
print(outputs)

sentence = "제주도 숙소 추천해 줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 숙소 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 독채 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 독채펜션 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 한달살기 숙소 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 게스트하우스 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 한달살기 게스트하우스 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 숙소 어디가 좋을까?"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "예쁜 제주도 숙소는 어디야?"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 예쁜 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 괜찮은 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 감성 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 편안한 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 분위기 좋은 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 가족끼리 갈만한 숙소 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 오션뷰 호텔 알려줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "괜찮은 제주도 숙소 어디야?"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 숙소 예쁜 곳 추천해 줘."
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 예쁜 숙소 알려줄래?"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 예쁜 숙소 추천 좀"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 예쁜 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 오션뷰 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 분위기 좋은 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 가족끼리 갈만한 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 바다 보이는 호텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 한달살기 숙소 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 풀빌라 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)

sentence = "제주도 모텔 추천"
jeju = ["제주", "애월", "제주서부", "제주동부", "서귀포", "하귀", "제주공항", "제주공항 근처", "성산일출봉 근처", "우도"]
outputs = [re.sub("제주도", x, sentence) for x in jeju]
print(outputs)