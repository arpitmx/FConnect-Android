# FConnect-Android
A flask api mini project

This flast + android application lets user to scan QR code from the laptop to connect it to the phone and then the user can control stuff using the android app on the laptop

<p float="left">

<img src="https://user-images.githubusercontent.com/59350776/163877966-76f2c67a-d20d-467f-94bd-327361a7f8cf.jpg" width="360" height="720">
<img src="https://user-images.githubusercontent.com/59350776/163877978-2162a886-9eed-4497-941e-9b9eb79cdee2.jpg" width="360" height="720">

</p>

https://user-images.githubusercontent.com/59350776/163876226-70afa55d-e31f-488f-a9ea-3d0f4045b642.mp4

Breakdown :
1. Flask server runs on localhost, listening for the inputs.
2. Ngrok tunnels the localhost to live internet creating a randomly generated subdomains example : https://www.123123123.ngrok.com/
3. QRhandler.py creates a QR code embedding the randomaly generated code of the subdomain. (qr = 123123123)
4. The app scans the QR code and get the subdomain , creates its original api link.
5. Connect with the server using the api link 
6. Sends requests and receives response.
