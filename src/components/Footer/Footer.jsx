import React from 'react';
import s from './Footer.module.css';

const Footer = () => {
    return (
        <footer className={s.footer}>
            <p>Footer is currently empty. Sorry. -^-</p> 
            <span>
            <div className={s.font_one}>font 1</div>
            <div className={s.font_two}>font 2</div>
            </span>
        </footer>
    )
}

export default Footer;