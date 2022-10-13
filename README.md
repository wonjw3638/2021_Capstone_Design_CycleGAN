# CycleGAN을 이용한 인터랙티브 웹페이지 (**Interactive Web using CycleGAN**)

📌 **목차**

1. **작품의 제작 동기**

2. **작품의 설계 및 구현**

   2.1 CycleGAN

   2.2 시스템 제작

   2.3 실험환경

   2.4 한계 및 개선

3. **작품의 구현 결과**
4. **작품의 기대 효과**

<br/>

---

<br/>

__✔ 작성 정보__

제  작  자 : 김지원, 정해정

지도교수 : 김동호

소        속 : 전자IT미디어공학과, 서울과학기술대학교 

환        경 : Windows 10, RTX 3080, Google Colaboratory nVIDIA tesla K80 GPU

개발도구 : Visual Studio Code, Python 3.8.5, Django 3.1.7

<br/>

---

<br/>

## 1. 작품의 제작 동기

우리는 사진의 전체적인 분위기를 보정하거나 필터를 적용하기 위해 다양한 편집 프로그램과 애플리케이션을 사용한다. 가끔 이러한 방식은 툴에 대해 사용 방법을 익혀야 할 때가 있고 시간이 많이 소요될뿐더러 얻은 결과물이 만족스럽지 않은 경우가 있다. 이에 우리는 위와 같은 고충을 해결하고 기술의 발전을 도모하기 위해, Image-to-Image translation 네트워크 중 CycleGAN 모델을 사용하여 이미지를 특정 타겟 도메인의 이미지로 변환하고 화질을 개선하여 인터랙티브 웹페이지를 통해 제공하는 구조의 서비스를 제안한다.

<br/>

사용자는 웹페이지를 통해 변환하고자 하는 이미지를 입력한다. CycleGAN은 입력된 이미지를 해당 도메인과 매핑되는 타겟 도메인의 이미지로 변환한다. 이후 특정 도메인에서 발생하는 화질 저하의 문제를 해결하고 전체적인 결과 이미지의 품질을 높이고자 RDN (Residual Dense Network)을 한 번 더 통과한다. 모든 과정을 거친 이미지는 웹페이지에서 인터랙티브로 동작할 수 있도록 구현된 기능들에 의해 사용자의 움직임에 따라 표시된다.

<br/>

우리는 CycleGAN을 이용한 인터랙티브 웹페이지를 통해 사진 색감 보정 및 필터 적용을 위한 방식 중 편리함을 극대화한 방법을 제공하고자 하였다. 또한, 쉽게 학습시켜 사용할 수 없는 딥러닝 모델을 실시간으로 서비스하여 인공지능 기술에 대한 사용자의 접근성을 높였다. 덧붙여 사용자와 간단하게 상호작용하며 동작할 수 있는 방식으로 흥미를 유발하였다.

<br/>

---

<br/>

## 2. 작품의 설계 및 구현

### 2.1. Cycle GAN

   우리가 본 작품에서 적용하는 CycleGAN은 적대적 생성 신경망이라고도 불리는 GAN(Generative Adversarial Network)을 기반으로 하여, 생성된 이미지가 실제 이미지와 통계적으로 거의 구분되지 않도록 하는 아주 실제 같은 합성 이미지를 생성한다. 이 때, CycleGAN은 서로 짝을 이루지 않는 데이터셋으로 학습시킬 수 있는 이미지 변환인 Unpaired Image-to-image translation에 해당하기 때문에, 유사성이 없는 이미지를 학습하되 순환 일관성 손실 함수를 추가하여 사용한다.

우리가 모델별로 생성기(Generator) 2개와 판별기(Discriminator) 2개를 학습하였다.

![image](https://user-images.githubusercontent.com/109324634/195487969-863e22eb-9fc2-4671-b17d-dc6ac3127dc5.png)

<br/>

특히 생성기의 경우 초반에는 이미지의 모양에 대한 변화가 큰 UNet 구조를 사용하여 학습을 진행하였으나, 모델의 학습 자체가 굉장히 불안정하여 성능이 매우 낮음을 확인하였다. 이에 우리는 ResNet 구조로 변경하여 안정적으로 학습할 수 있도록 하였다. ResNet에서는 9개의 residual block을 사용하였고, encoder와 decoder를 연결하는 skip connection을 구성해주었다.  



**[ UNet ]**

![image](https://user-images.githubusercontent.com/109324634/195488032-f745331c-65de-49bb-b27d-a9ca4db373d3.png)

![image](https://user-images.githubusercontent.com/109324634/195488065-90db613e-9734-40a6-b72a-454f54517b28.png)



**[ ResNet ]**

![image](https://user-images.githubusercontent.com/109324634/195488172-fd946b90-2648-401c-abc9-d68805ffa49a.png)

![image](https://user-images.githubusercontent.com/109324634/195488199-75bf429b-8dab-4d6c-9487-6a1efc8896cc.png)



### 2.2 시스템 제작

수많은 이미지 변환 모델 중 CycleGAN을 선택한 이유는 학습 데이터를 수집하는 과정에서 생길 수 있는 어려움을 최소화하기 위함이다. 앞서 언급한대로 CycleGAN은 서로 짝을 이루지 않는 데이터셋으로 학습시킬 수 있는 이미지 변환인 Unpaired image-to-image translation에 해당하는 네트워크이고, Patch 단위로 훈련을 진행한다. 따라서 현실적으로 수집하기 어려운 Paired dataset을 구하는 문제점을 해결할 수 있고, 비교적 적은 양의 데이터로 안정적인 결과 이미지를 얻는 것이 가능하다. CycleGAN은 객체의 모양은 바꿀 수 없다는 단점이 존재하나, 이미지의 전체적인 분위기 및 스타일을 변환하고자 하는 우리의 목표에는 큰 문제가 되지 않는다고 판단하였다.

 

 이미지의 도메인은 낮과 밤, 봄과 가을, 여름과 겨울 도메인에서 상호변환 할 수 있도록 설정하여 총 3개의 모델을 생성하였다. 각각에 해당하는 데이터셋을 수집하기 위해 Google에서 데이터를 크롤링하여 저장하였고, Tensorflow에서 제공하는 데이터셋 중 CycleGAN 논문에서 사용한 summer2winter_yosemite 데이터를 사용하였다. 그리고 공공데이터포털에서 지역관광공사와 국립공원공단이 제공하는 데이터를 활용하여, 실제 서비스 제공 시 입력될 이미지를 고려해 우리나라 풍경을 학습할 수 있게 하였다. 이후 데이터 증강을 위해 좌우변환, 확대, 랜덤 크롭 및 채도 조정을 수행하였다. 데이터 중 80%는 훈련에 사용하고 20%를 시험에 사용하였다.

![image](https://user-images.githubusercontent.com/109324634/195488365-23587254-10ae-4a91-b58d-b2065f835914.png)

 수집한 데이터는 Tensorflow Datasets API를 사용하여 모델에 입력하기 위한 Custom dataset으로 변환한다. 이 때 모델에 따라 train, test 폴더를 각각 생성한 후 학습, 평가에 사용할 데이터셋을 저장하고, metadata 파일을 생성해주어 데이터의 위치, 이름, 도메인 등을 저장해준다. 이후 custom dataset.py을 통해 데이터셋 feature 및 설명을 정의하고, 파일들을 읽어들여 train, test에 사용할 데이터를 나눌 수 있도록 설명하고, 각 example을 생성하는 generator을 정의해준다.

 

 사용자에게서 input image를 받은 후, CycleGAN으로 변환된 이미지를 인터랙티브 웹페이지를 통해 보여주는 것이 본 시스템의 최종 목표이다. CycleGAN code의 사용을 용이하게 하기 위해서 python code를 사용하는 Django를 선택하여 Backend를 구성하였다.

 사용자에게서 받은 이미지를 저장할 수 있는 Database를 생성하였다. CycleGAN의 입력 이미지는 256x256 pixel이어야 한다는 조건이 있으므로, 사용자가 원하는 영역을 1:1 비율로 crop 할 수 있도록 하였다. 1:1로 크롭된 이미지는 256x256으로 resize 변환과정을 거친 후에, 학습된 모델을 통해 이미지 변환을 거치게 된다.

 사용자가 입력한 이미지가 어떠한 도메인인지를 선택하면 그에 따른 모델로 변환시켜준다. 후에 변환된 이미지는 인터랙티브 Web을 통해 확인할 수 있다. 낮↔밤 변환은 Drag에 따른 Scratch 반응을 보인다. 봄↔가을 변환은 마우스 hover에 따른 blur 반응을 보인다. 여름↔겨울 변환은 Scroll에 따라 이미지가 나타나게 된다. 인터랙티브 Web을 경험한 후에는 변환된 이미지를 다운로드 받을 수 있도록 하였다.



### 2.3 실험 환경

작품에서 제안하는 시스템을 구현하기 위해서는 GPU를 탑재한 PC가 필요하다. Intel(R) Core(TM) i7-5960X CPU @ 3.00GHz 및 RTX 3080 을 탑재한 Window10 64비트 운영체제를 기반으로 하는 PC를 사용 하였다. 그리고 Google이 제공하는 Google Colaboratory의 nVIDIA tesla K80 GPU 환경에서 학습을 진행하였다. 각 모델당 200 epoch 동안 학습하였고, 환경과 데이터셋의 크기에 따라 5시간에서 이 주일 정도의 시간이 소요되었다.

 인터랙티브 Web을 구현하기 위해서 Django v3.1.7, Python v3.8.5을 사용하였다.



### 2.4 한계 및 개선

학습 과정을 checkpoint로 확인한 결과 작은 epoch에서는 checkerboard artifact나 타겟이 아닌 곳에서의 왜곡이 발생했으나, 전반적으로 epoch이 증가하면서 개선되었다. 그러나 낮 ↔ 밤 변환 모델에서 이미지 도메인의 특징으로 인해 화질의 저하가 눈에 띄게 나타나는 것을 확인하였다. 이 문제를 해결하고 특정 모델뿐만 아니라 전체 시스템의 품질을 높이고자 RDN (Residual Dense Network) 모델을 사용하여 화질을 개선하였다. RDN은 image super resolution을 위해 residual dense block (RDB)을 사용하여 충분한 양의 local feature을 추출하는 방식을 사용한 모델이다. RDN의 학습된 가중치를 사용할 수 있는 네트워크 중 우리의 이미지에 적용했을 때 성능이 가장 뛰어난 noise-cancel 모델의 가중치를 사용해 화질 개선을 수행하였다. 비교를 위해 RDN으로 화질을 개선한 이미지, RDN을 통과한 후 Edge sharpening을 수행한 이미지, ESRGAN 모델을 적용한 이미지 총 3개의 PSNR을 측정해 비교하고, 추가적으로 주관적인 선호도를 평가한 결과 RDN만 적용한 버전을 최종적으로 선택하였다.



## 3. 작품의 구현 결과

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

![image](https://user-images.githubusercontent.com/109324634/195489100-792b2b29-8251-4d76-8baa-1fc94327d319.png)

**Hover page**

![image](https://user-images.githubusercontent.com/109324634/195489123-6529ce24-b7e0-4710-8017-0804411ff690.png)

**Scroll page**

![image](https://user-images.githubusercontent.com/109324634/195489147-69978a9c-3ca3-46f0-9190-e695a2f24a4d.png)

CycleGAN을 학습한 모델을 사용하여, 웹 흐름도를 바탕으로 웹 페이지를 구현하였다. 그 결과 사용자가 손쉽게 원하는 이미지를 crop하여 upload할 수 있었고, 학습한 모델을 바탕으로 이미지를 변환할 수 있었다. 또한, 인터랙티브 웹 페이지 구현 결과에서 이를 확인할 수 있었고, 변환된 이미지를 다운로드 할 수 있었다.



## 4. 작품의 기대효과

결론적으로 본 작품에서는 CycleGAN을 이용한 인터랙티브 웹페이지를 통해 사용자가 보다 쉽게 인공지능 기술을 사용하여 이미지를 변환하는 시스템을 제안하였다. 시스템에 더 다양한 모델을 학습시킨다면 사용자는 이미지 보정 및 편집과 같은 별도의 과정 없이도 자신이 원하는 이미지를 손쉽게 얻을 수 있다. 본 작품의 시스템을 이미지뿐만 아니라 video, 360영상, AR/VR등의 미디어에 적용 시킨다면 한정된 이미지 자원을 사용하여 더 다양한 서비스를 사용자에게 제공할 수 있을 것이다.













