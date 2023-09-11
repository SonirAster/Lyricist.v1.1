import React from 'react';
import s from './PageContent.module.css';
import SearchPanel from '../SearchPanel/SearchPanel';

const PageContent = () => {
    return (
        <div className={s.page__wrapper}>
            <SearchPanel />
            <span>New Test App</span>
        </div>
    )
}

export default PageContent;