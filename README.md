## Github Repositories ##
Source code derived from: 
[[Duan's Repository](https://github.com/duanzhiihao/RAPiD#readme)],
[[Tezcan's Repository](https://github.com/ozantezcan/RAPiD-T.git)],
[project website - RAPiD](https://vip.bu.edu/projects/vsns/cossy/fisheye/rapid/),
[project website - RAPiD-T](https://vip.bu.edu/projects/vsns/cossy/fisheye/rapid-t/) 

## Requirements ##
* [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
The following packages were imported in a Linux Environment:
* [pytorch 1.9.0](https://pytorch.org/get-started/locally/)
* [opencv 4.5.0](https://opencv.org/opencv-4-5-0/)
* [pycocotools](https://github.com/cocodataset/cocoapi)
* tqdm

## Testing ##
1. Clone my repository
2. Download the [pre-trained network weights](https://github.com/duanzhiihao/RAPiD/releases/download/v0.1/pL1_MWHB1024_Mar11_4000.ckpt), which is trained on COCO, MW-R, HABBOF, CEPDOF and weights of trained models from [Google Drive](https://drive.google.com/drive/folders/1G66FOZT4gY56cw63twANtS_Tqf3j5AtO?usp=sharing). Place these weight files in `weights` folder.
If running in Virtualbox Machine in Ubuntu:
3. Refer to [OpenCV Installation](https://pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/) to install openCV on Ubuntu.
4. Run `workon -openCV setup name-` in terminal.

<p align="center">
<img src="https://github.com/duanzhiihao/RAPiD/blob/master/images/readme/exhibition_rapid608_1024_0.3.jpg?raw=true" width="500" height="500">
</p>

## Uploading Files with Flask ##

## How to Run the App Locally

## Using Pipenv

1. Modify the `Pipfile` to specify your version of Python 3
1. Install Flask: `pipenv install`
1. Activate the virtual environment: `pipenv shell`

## Using virtualenv and pip

1. Create the virtual environment: `virtualenv -p python3 env`
1. Activate the virtual environment: `source env/bin/activate`
1. Install Flask: `pip install Flask`

## Start Flask

Enter these two commands in your terminal:

`export FLASK_APP=app`

`flask run`


## Citation
```
Z. Duan, M.O. Tezcan, H. Nakamura, P. Ishwar and J. Konrad, 
“RAPiD: Rotation-Aware People Detection in Overhead Fisheye Images”, 
in IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 
Omnidirectional Computer Vision in Research and Industry (OmniCV) Workshop, June 2020.

RAPiD-T source code is available for non-commercial use. If you find our code and  [WEPDTOF dataset](https://vip.bu.edu/projects/vsns/cossy/datasets/wepdtof/) useful or publish any work reporting results using this source code, please consider citing our paper

M.O. Tezcan, Z. Duan, M. Cokbas, P. Ishwar, and J. Konrad, “WEPDTOF: A Dataset and Benchmark 
Algorithms for In-the-Wild People Detection and Tracking from Overhead Fisheye Cameras” 
in Proc. IEEE/CVF Winter Conf. on Applications of Computer Vision (WACV), 2022.

```
