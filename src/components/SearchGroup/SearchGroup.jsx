import React from 'react';
import s from './SearchGroup.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const src = 'http://localhost:8000/group';
const SearchGroup = () => {
    return (
        <div className={s.searchGroup}>
            search group
        </div>
    )
}

// const getGroups = () => {
//     const [groups, setGroups] = useState([]);
//     useEffect(() => {
//         axios
//             .get(src)
//             .then(res => {
//                 setGroups(res.data);
//             })
//             .catch(err => {
//                 console.log(err);
//             }).then(i => {
//                 console.log(i);
//                 return i;
//             }
//             )
//     }, []);
//     return (
//         <div>
//             {groups.map(group => {
//                 return (
//                     <p>{group}</p>
//                 );
//             })}
//         </div>
//     )

// }

export default SearchGroup;