# 인수인계 (Handoff) — Jun Lee 시애틀 마켓 대시보드

다른 AI / 사람이 이어서 작업할 때 이 파일부터 읽으세요.

## 누구 / 무엇
- Jun Lee, Compass 부동산 브로커 (Greater Seattle). 425.766.9692 · junleeproperties.com · 영어/한국어/중국어
- 한국어 커뮤니티(카톡 단톡방)와 영어 손님용 시장 지표 웹페이지 + 월간 PDF 리포트

## 결과물
| 무엇 | 위치 |
|---|---|
| 라이브 웹페이지 | https://junleeproperties.github.io/seattle-market/ (영어: `?lang=en`) |
| 저장소 | github.com/JunLeeProperties/seattle-market (GitHub Pages, main 브랜치 루트) |
| 월간 PDF 리포트 (2026년 10월, 21쪽) | Jun이 갖고 있음: JunLee_Market_Report_2026-10_v2.pdf (Claude Design 캔버스에서 편집함) |

## 파일 구조
- `index.html` — 빌드 결과(직접 고치지 말 것). `src/build.py` 실행으로 생성
- `notes.json` — **모든 분석·의견 문장**. 페이지가 실행 중에도 이 파일을 읽어 반영
  - `areas.<도시ID>`: `label/tag/cls`(판정), `sub`(한 줄 요약), `read`(데이터 분석 4문장, 합니다체), `watch`(다음 달 볼 것), `jun_buy/jun_sell/jun_memo`(Jun의 의견, 해요체 — 현재는 Claude 초안, Jun이 직접 바꿀 예정)
  - `weekly.<King|Snohomish|Pierce>`: 이번 주 읽기
  - `en`: 위와 같은 구조의 영어 버전
- `src/template.html` — 페이지 원본 (자리표시 `__LOGO__ __FACE__ __QR__ __DATA__ __WEEKLY__ __NOTES__`)
- `src/data.json` — 17개 지역 월간 데이터 (카운티 3 + 도시 14). NWMLS 시계열 2024-01~2026-10(34개월, 인덱스 33=2026년 10월), 도시 가격(p)은 Redfin 3개월 기준
- `src/weekly.json` — 주간 데이터 배열 `[{start,end,King:[신규,펜딩,거래,가격인하,취소],...}]`
- `src/img.json` — 로고/사진/QR base64
- 빌드: `python3 src/build.py` → `index.html` 생성 → commit & push → 1~2분 뒤 반영

## 정기 업데이트
- **매주**: Jun이 카운티별 주간 카드 이미지 3장(NWMLS)을 줌 → `src/weekly.json`에 한 주 추가 → `notes.json`의 `weekly`(+`en.weekly`) 문장 갱신 → 빌드·푸시. 증감율은 자동 계산. 카드의 %와 직접 계산이 다르면 Jun에게 확인 (11/2~9 피어스 가격인하 222 vs 카드 3%↓ 불일치 확인 대기 중)
- **매월**: Jun이 NWMLS InfoSparks에 로그인 → 3개 카운티·14개 도시 지표 수집, Redfin 도시 페이지에서 가격 → `src/data.json` 갱신 → 17개 지역 분석 문장 재작성 → 빌드·푸시, PDF 리포트도 새로 제작
  - 다음 달 할 일: 시애틀은 단독주택/콘도를 나눠 받아 "콘도 재고" 가설 확인

## 마켓 리포트 PDF + QR
- QR → https://junleeproperties.github.io/seattle-market/report/ (고정 주소, QR 재인쇄 불필요)
- 매달: `report/YYYY-MM.pdf` 추가 → `report/reports.json`에 `{"file":"YYYY-MM.pdf","ym":"YYYY-MM","pages":N}` 한 줄 추가 → 푸시. 최신 달이 자동으로 맨 위, 나머지는 '지난 리포트'로 쌓임

## 판정 방식
재고 소진 기간·판매 소요일·최초 리스팅가 대비를 그 지역 예년(2024·2025년 9~11월 평균, 인덱스 8,9,10,20,21,22)과 비교. msi/dom ±15%, po ±0.8%p → 신호 점수. 거기에 거래 건수·새 매물·가격 흐름을 사람이 보고 최종 판정(뚜렷/기우는 중/신호 엇갈림)을 `notes.json`에 적음.

## Jun의 요청 스타일
- 리포트는 데이터 중심, AI 평가 금지. 의견은 "Jun의 의견" 칸에만, Jun 본인 말로
- 한국어: 데이터 설명은 따뜻한 "~합니다", Jun 의견은 "~해요". 딱딱하거나 번역투 금지
- 메기(seattlemaggiesun) 리포트 참고하되 베끼지 말 것

## 남은 일
- Jun의 의견 17개를 Jun 본인 말로 교체 (현재 초안)
- (선택) market.junleeproperties.com 연결: DNS CNAME `market` → `junleeproperties.github.io` 추가 후 저장소에 `CNAME` 파일
- NWMLS 데이터 공개 게시 규정 확인
