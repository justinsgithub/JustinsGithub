var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'justinaawd@gmail.com',
    pass: 'jjgjxlwssscepmku'
  }
});

var mailOptions = {
  from: 'justinaawd@gmail.com',
  to: 'lemonjewell@yahoo.com',
  subject: 'Automated Emails(:',
  text: 'How Lit'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
}); 
