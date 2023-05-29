import React from "react";
import { Bullet } from '@ant-design/plots';

export const TemperatureBullet = ({ current }) => {
    const data = [
        {
            title: '',
            ranges: [45, 70, 85],
            measures: [current],
            target: 85,
        },
    ];
    const config = {
        data,
        measureField: 'measures',
        height: 10,
        padding: 10,
        rangeField: 'ranges',
        targetField: 'target',
        xField: 'title',
        color: {
            range: ['#bfeec8', '#FFe0b0', '#FFbcb8'],
            measure: '#5B8FF9',
            target: '#FFbcb8',
        },
        xAxis: {
            line: null,
        },
        yAxis: false,
        label: {
            target: true,
        },
    };
    return <Bullet {...config} style={{ marginBottom: 40, marginTop: 40 }} />;
}