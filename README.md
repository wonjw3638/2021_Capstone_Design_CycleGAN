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

제  작  자 : 김지원(17101446), 정해정(17101532)

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

![image-20220729171115136](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220729171115136.png)

<br/>























































