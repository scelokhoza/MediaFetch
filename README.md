# MediaFetch

< MediaFetch is a program that can download videos and audios from differnt webistes like youtube, linkeding, x, instagram and tiktok using their url and also allows you to search for a song then download it from there >

========================================HOME PAGE==========================================
![home-page](https://github.com/user-attachments/assets/57da7b39-eda0-4d0e-9404-68897612c8a7)

========================================DOWNLOAD BY URL==========================================
![selection-page](https://github.com/user-attachments/assets/4ca445d1-5d41-4623-966e-51efa8e9a7cb)

========================================SEARCH AND DOWNLOAD==========================================
![search](https://github.com/user-attachments/assets/2992294d-b018-4202-9eba-f75c8cff7d52)







**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Author](#author)
- [Change log](#change-log)
- [License](#license)

## Installation

On macOS and Linux:

```sh
$ git clone git@github.com:scelokhoza/MediaFetch.git
```

On Windows:

```sh
PS> git clone git@github.com:scelokhoza/MediaFetch.git
```

## Execution / Usage

To run < MediaFetch >, fire up a terminal window and run the following command:

```sh
$ cd MediaFetch
$ pip install -r requirements.txt
$ python3 download_media.py
```
You should see an ouput like this in your terminal:
![execute](https://github.com/user-attachments/assets/670798a9-cc94-4aab-98a0-1f307e245906)

Copy and paste the [`http:127.0.0.1:5000`] link to your browser of choice



For more examples, please refer to the project's [Wiki](wiki) or [documentation page](docs).


## To Test

To run all the unittests: ```sh $ python3 -m unittest tests/test_download_media.py```

To run a specific unittests, e.g test_formats_audio: ```sh $ python3 -m unittest tests.test_download_media.TestMediaDownload.test_formats_audio```


## Technologies

< MediaFetch > uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- [HTML](https://html.com/): ![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- [CSS](https://css-tricks.com/): ![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- [AJAX](https://api.jquery.com/jQuery.ajax/): ![AJAX](https://img.shields.io/badge/AJAX-1572B6?style=for-the-badge&logo=ajax&logoColor=white)

## Features

< MediaFetch > currently has the following set of features:

- Can download [Audio]() by url from the sites below
- Can download [Video]() by url from the sites below
- Allows you to search and download a song of your choice

< MediaFetch can download audio/video by url from these sites for now>

- Support for [Tiktok](https://img.shields.io/badge/tiktok-3670A0?style=for-the-badge&logo=tiktok&logoColor=ffdd54)
- Support for [Facebook](https://img.shields.io/badge/facebook-3670A0?style=for-the-badge&logo=facebook&logoColor=ffdd54)
- Support for [X](https://img.shields.io/badge/x-3670A0?style=for-the-badge&logo=x&logoColor=ffdd54)
- Support for [Youtube](https://img.shields.io/badge/youtube-3670A0?style=for-the-badge&logo=youtube&logoColor=ffdd54)
- Support for [Linkedin](https://img.shields.io/badge/linkedin-3670A0?style=for-the-badge&logo=linkedin&logoColor=ffdd54)
  
## Contributing

To contribute to the development of < project's name >, follow the steps below:

1. Fork < MediaFetch > from <https://github.com/scelokhoza/MediaFetch/fork>
2. Create your feature branch (`git checkout -b feature-new`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some new feature'`)
5. Push to the branch (`git push origin feature-new`)
6. Create a new pull request

## Contributors

Here's the list of people who have contributed to < project's name >:

- Scelo Khoza – [@MnikaziWempuphuh](https://x.com/mnikaziwempuphuh) – sceloprince749@gmail.com
- Nhlanhla Modingoane – nmodingoane023@student.wethinkcode.co.za

The < MediaFetch > development team really appreciates and thanks the time and effort that all these fellows have put into the project's growth and improvement.

## Author

< Scelo Khoza > – sceloprince749@gmail.com

## Change log

- 0.0.2
    - Polish the user interface
- 0.0.1
    * First working version


## License

< MediaFetch > is distributed under the [`BSD-2-Clause license`] license. See [`LICENSE`](https://unlicense.org) for more details.
