# Flask-Mail-Test
中国区在使用Flask-Mail插件发送邮件总会遇到问题，所以纪录自己的解决方案。

### 大坑慎入！！！
最近一直在折腾`Falsk Mail`插件，由于在国内，想使用谷歌服务器发送邮件时不时遇到各种bug。最后我实在受不了，打算更换为国内的邮件服务器。但是一直会遇到各种问题。
问题一：
```
ssl.SSLError
SSLError: [SSL: UNKNOWN_PROTOCOL] unknown protocol (_ssl.c:590)
```
解决方案：
错误跟SSL相关，知道我在网上看到了[这篇教程][1]，我才恍然大悟。当我们不使用`app.config['MAIL_USE_SSL'] = False`时，一定要把邮件端口号设置为`app.config['MAIL_PORT'] = '25'`。如果你启用了`ssl`,那么请把端口号设置为465！。不然一定会遇到上面的错误。

然而事情并没有结束。。。
我们可能会遇到这样的错误：
```
smtplib.SMTPAuthenticationError
SMTPAuthenticationError: (530, 'Error: A secure connection is requiered(such as ssl). More information at http://service.mail.qq.com/cgi-bin/help?id=28')
```
当时我就懵逼了。不过从错误提示信息可以看到需要我们启用ssl协议。但是请记住上面的话，启用ssl协议，一定要把相应的端口号改为465，否则你有回到上一个错误。
 当然安全的链接并不只有一个。我们可以使用`app.config['MAIL_USE_TLS'] = True`.也就是`TLS`协议，但是此时要记住端口号要改为25！！！

你肯定以为错误到这里就结束了，然而底下还有一个坑：
此处只针对qq邮箱。首先我们要开启SMTP服务，开启的过程中会得到一个授权码。这个授权码就是`app.config['MAIL_PASSWORD'] = 'nwntuhwdkrrbbbbe'`.而不是你认为的`qq`密码。一定要切记。

最后简单的总结下：`SSL`协议搭配端口号`465`，`TSL`协议搭配端口号`25`。不论使用哪个协议，都要打开`SMTP`服务。哎，总之是一把辛酸泪。
