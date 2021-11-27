import React from 'react'
import styles from './authorization-form.module.css'

class Contact extends React.Component {
     constructor(props) {
    super(props);
    this.state = {
      password: 'password',
      authorized: false
    };
    this.authorize = this.authorize.bind(this);
  }

  authorize(e) {
    const password = e.target.querySelector(
      'input[type="password"]').value;
    const auth = password == this.state.password;
    this.setState({
      authorized: auth
    });
  }

  render() {
    const login = (
    <form action="#" className={styles.ul} onSubmit={this.authorize}>
<input  className={styles.input} type="password" placeholder="Password"/>
<input className={styles.input} type="submit"/>
    </form>
    )
    const contactInfo = (
 <ul className={styles.ul}>
          <li>
        little lemons nudes
          </li>
          <li>
        little lemons premium content
          </li>
          <li>
send a message
          </li>
        </ul>
);
    return (
      <div className={styles.div} id="authorization">
        <h1 className={styles.h1}>{this.state.authorized && 'Contact' || 'Enter the Password'}</h1>
          { this.state.authorized ? contactInfo : login }

      </div>
    );
  }
}
export default Contact;
