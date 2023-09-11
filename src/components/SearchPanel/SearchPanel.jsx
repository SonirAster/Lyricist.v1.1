import React from 'react';
import s from './SearchPanel.module.css';
import {NavLink} from 'react-router-dom';

const SearchPanel = () => {
    return (
        <div className={s.search_panel}>
            <div className={s.search_group}>
                <NavLink to="/group" className={s.activeLink}>Seek for Group</NavLink>
            </div>
            <div className={s.search_song}>
            <NavLink to="/group" className={s.activeLink}>Seek for Song</NavLink>
            </div>
        </div>
    )
}

export default SearchPanel;
