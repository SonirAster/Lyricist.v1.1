import React from 'react';
import s from './NoContent.module.css';

const NoContent = () => {
    return (
        <div className={s.no_content_message}>
            <span>No content here</span>
            <div>-^-</div>
        </div>
    )
}

export default NoContent;