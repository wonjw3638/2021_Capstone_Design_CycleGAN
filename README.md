# 🖼 CycleGAN을 이용한 인터랙티브 웹페이지 (**Interactive Web using CycleGAN**)

## 🚧 수정 예정

- [x] README 수정하기
- [ ] Modl Form으로 구현하기
- [ ] Front-End 반응형 웹 페이지 구현하기
- [ ] Front-End 디자인 요소 넣기
- [ ] `get_objects_404` 로 정상적인 값이 들어오지 않은 경우 404반환하기

<br>

__✔ 작성 정보__

제  작  자 : 김지원, 정해정

지도교수 : 김동호

소        속 : 전자IT미디어공학과, 서울과학기술대학교 

환        경 : Windows 10, RTX 3080, Google Colaboratory nVIDIA tesla K80 GPU

개발도구 : Visual Studio Code, Python 3.8.5, Django 3.1.7

<br/>

✔ **프로젝트 목표**

사용자가 업로드한 이미지를 CycleGAN을 사용해 스타일을 변환하여 반환받을 수 있는 웹 페이지

---

<br/>

## 🔹 제작 동기

이미지의 분위기를 보정하거나 필터를 적용하기 위해 다양한 편집 프로그램을 사용한다. 그러나 이런 프로그램들은 사용방법을 익히기 어렵고, 사용방법이 익숙해지지 않으면 만족스러운 결과물을 내기에 굉장히 많은 시간이 걸린다. 이러한 불편함을 해소하고자 이미지 스타일을 변환해주는 웹 페이지를 제작해보았다.

이미지를 변환한 후에는 단순히 반환하는 것이 아닌, 사용자와 상호작용 할 수 있는 동적인 웹을 만들고자 하였다.



## 🔹 CycleGAN 모델 개선

**[ UNet ]**

![image](https://user-images.githubusercontent.com/109324634/195488032-f745331c-65de-49bb-b27d-a9ca4db373d3.png)

![image](https://user-images.githubusercontent.com/109324634/195488065-90db613e-9734-40a6-b72a-454f54517b28.png)



**[ ResNet ]**

![image](https://user-images.githubusercontent.com/109324634/195488172-fd946b90-2648-401c-abc9-d68805ffa49a.png)

![image](https://user-images.githubusercontent.com/109324634/195488199-75bf429b-8dab-4d6c-9487-6a1efc8896cc.png)

ResNet 구조를 사용하여 성능을 개선시켰다.



## 🔷 구현결과

**구현 결과 : 낮 → 밤**

![image](https://user-images.githubusercontent.com/109324634/195488501-49d841b6-6927-4bdc-99d9-28b441d6c217.png)

**구현 결과 : 밤 → 낮**

![image](https://user-images.githubusercontent.com/109324634/195488527-ceae60c3-0db8-454e-a8be-25aa7bdae9e7.png)

**구현 결과 : 봄 → 가을**

![image](https://user-images.githubusercontent.com/109324634/195488547-b60f8bad-4206-4e0b-8c1d-6a6b245dc58b.png)

**구현 결과 : 가을 → 봄**

![image](https://user-images.githubusercontent.com/109324634/195488591-04208838-5934-4c00-adfe-49fe96832dfc.png)

**구현 결과 : 여름 → 겨울**

![image](https://user-images.githubusercontent.com/109324634/195488614-59a1a65d-0235-472c-8192-1b0c1c537aed.png)

**구현 결과 : 겨울 → 여름**

![image](https://user-images.githubusercontent.com/109324634/195489805-38c625a2-00ba-41f2-9dab-e3a4214059f0.png)



**[ 웹 흐름도 ]**

![image](https://user-images.githubusercontent.com/109324634/195488964-309e68fa-38f6-41cd-9031-8d421ccead12.png)

**[ 웹 페이지 구현 결과 ]**

**Drag page**

사용자는 낮 사진은 밤 사진으로, 밤 사진을 낮 사진으로 변환할 수 있으며, 변환된 결과물을 마우스의 Drag에 반응해 확인할 수 있게 된다.

download > 이미지를 다운로드 할 수 있다.

return > 새로운 이미지를 업로드 한다.

![image](https://user-images.githubusercontent.com/109324634/195489100-792b2b29-8251-4d76-8baa-1fc94327d319.png)

**Hover page**

사용자는 봄 사진은 가을 사진으로, 가을 사진을 봄 사진으로 변환할 수 있으며, 변환된 결과물을 마우스의 hover에 반응해 확인할 수 있게 된다. blur 처리되어있던 이미지는 mouse의 hover에 반응해 선명하게 나타난다.

download > 이미지를 다운로드 할 수 있다.

return > 새로운 이미지를 업로드 한다.

![image](https://user-images.githubusercontent.com/109324634/195489123-6529ce24-b7e0-4710-8017-0804411ff690.png)

**Scroll page**

사용자는 여름 사진은 겨울 사진으로, 겨울 사진을 여름 사진으로 변환할 수 있으며, 변환된 결과물을 Scroll의 움직임에 따라 이미지가 나타나는 것으로 확인할 수 있게 된다.

download > 이미지를 다운로드 할 수 있다.

return > 새로운 이미지를 업로드 한다.

![image](https://user-images.githubusercontent.com/109324634/195489147-69978a9c-3ca3-46f0-9190-e695a2f24a4d.png)

## 🔷 회고

- Django를 사용해 쉽게 웹 페이지를 구현할 수 있었다.
- 머신러닝을 사용해 웹 페이지를 제작한 경험은 처음이어서 많은 시행착오를 거쳤다. 그럼에도 원하는 기능을 구현할 수 있었다.
- 머신러닝을 사용한 웹 페이지를 구현하기 위해서는 개발환경 체크가 매우 중요하다.













