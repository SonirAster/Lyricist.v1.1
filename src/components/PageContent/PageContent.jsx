import React from 'react';
import s from './PageContent.module.css';
import { Routes, Route } from 'react-router-dom';
import MainContent from '../MainContent/MainContent';
import SearchSong from '../SearchSong/SearchSong';
import SearchGroup from '../SearchGroup/SearchGroup';
import SearchPanel from '../SearchPanel/SearchPanel';

const PageContent = () => {
    return (
        <div className={s.page__wrapper}>
            <SearchPanel />

            <Routes>
                <Route path='/' element={<MainContent />} />
                <Route path='/group' element={<SearchGroup />} />
                <Route path='/song' element={<SearchSong />} />
            </Routes>
        </div>
    )
}

export default PageContent;

