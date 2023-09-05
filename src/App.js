import axios from 'axios';
import styles from './App.css';
import React from 'react';

class App extends React.Component{
    state = { details: [], }

    componentDidMount(){
        let data;
        axios.get('http://localhost:8000')
        .then(res => {
            data = res.data;
            this.setState({
                details: data
            });
        })
        .catch(err => {
            console.log(err);
        })
        // data =  '1';
        // console.log(data);
        //version11
    }
    render() {
        return (
            <div>
                <span>New Test App</span>
                {this.state.details.map((output, id) => (
                    <div key={id}>
                        <h2 className={styles.dd}>{output.title}</h2>
                        <p>{output.channel}</p>
                    </div>
                ))}
            </div>
        )
    }

}

export default App;

