# FitBoi
## Smart Physical Health Advisor

FitBoi takes an uploaded image and some basic BMI (Body Mass Index) info and
creates workout advice tailored to YOU. FitBoi is an easy tool meant to improve
the physical health of its users.

This app uses a convolution neural network to recognize your uploaded image and
measure your body fat percentage. It does this by using django and Google's Cloud API. 
(Revision needed)

## To Start:

    ./clear_DB.sh
    cd fitboitech
    python manage.py runserver
    python manage.py migrate
    http://localhost:8000/fitboi

## Authors
* **Kieran** [kduggan15](https://github.com/kduggan15)
* **Jonathan** [jontran1](https://github.com/jontran1)
* **Michael** [msalamonski](https://github.com/msalamonski)
* **Bon** [bonliu](https://github.com/bonliu)

### TODO:
- Set index.html as homepage
- ...

---

# Lehman-Hackathon-2019
Repository for Lehman Hackathon 2019
## Ideas
1. Sustainable future
2. End poverty
3. zero hunger
4. **good health**
5. quality education
6. clean water
7. Affordable and clean energy
8. climate action
9. sustainable communities and cities
10. creating more partnerships

## Uploading images in Django
[geekforgeek](https://www.geeksforgeeks.org/python-uploading-images-in-django/)
### Helpful dev tips
[Working with Git Branches](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches)
#### Safely merge branch

    git checkout master
    git pull origin master
    git merge test
    git push origin master
