import React from 'react';
import s from './Header.module.css';
import { NavLink } from 'react-router-dom';

const Header = () => {
    return (
        <div className={s.header}>
            <div>
                Find any group or song You seek with
                <span><NavLink to={'/'}> Lyricist.com</NavLink>!</span> 
            </div>
        </div>
    )
}

export default Header;