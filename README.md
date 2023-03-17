# Ad Registration Service

<!-- ABOUT THE PROJECT -->
## About The Project

In this project we implement an ad registration service, using cloud services for implementing database, object storage, object detection, and mail sending.

This project is for 'Cloud Computing' course in university and the purpose of this exercise is to get to know and work with cloud service.

### Built With

APIs implemented by:
 - FastAPI
 
The services used in this project are:

- DBaaS: Postgres provided by [Liara](https://liara.ir/)
- Object storage (S3): Provided by [Parspack](https://parspack.com/)
- RabbitMQ: Provided by [CloudAMQ](https://www.cloudamqp.com/)
- Image processing (object detection): Provided by [Imagga](https://imagga.com/)
- Mailing: Provided by [Mailgun](https://www.mailgun.com/)

 ### Structor of projcet:
 
  This project consict of two services: 
  
   1. The first service contains API for communicating with user (get input or show the final result) and forward user requests to queue.
   2. The second service check the RabbitMQ queue and process the new input image and return the final result to fisrt image


<!-- GETTING STARTED -->
## Getting Started
1. install requirements
  ```sh
  pip install -r service-1/requirements.txt
  ```
   if you want to run each service on different VM run the following on the VM for second servise, too.
  ```sh
  pip install -r service-1/requirements.txt
  ```
2. run services
  ```sh
  python service-1/src/main.py 
  pyhton service-2/src/main.py
  ```
3. use it!

   open browser and go to [http://localhost:8000/#docs/](http://localhost:8000/#docs/)

