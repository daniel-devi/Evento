import React from 'react';
import { useState, useEffect } from 'react';
import api from '../../utils/Api';

function Home() {
    const [data, setData] = useState([]);

    useEffect(() => {
        api.get("").then((response) => {
            console.log(response);
            console.log(response.data);
            setData(response.data.features);
        })
    }, [])
    return (
        <div>
            {data.map((item, index) => (
                <p key={index}>{item}</p>
            ))}
        </div>
    );
}

export default Home;