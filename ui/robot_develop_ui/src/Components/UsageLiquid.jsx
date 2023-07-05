import React from "react";
import { Liquid } from '@ant-design/plots';
import { Space, Typography } from 'antd';

const { Text } = Typography;

export const UsageLiquid = ({ percent, title, color, theme }) => (
    <Space direction='vertical' align='center'>
        <Liquid {...{
            color: color,
            width: 200,
            height: 200,
            percent: percent,
            statistic: {
                content: {
                    style: {
                        fill: "#fff" ? theme === "dark" : "#000"
                    },
                },
            },
            outline: {
                border: 4,
                distance: 2,
            },
            wave: {
                length: 128,
            }
        }} />
        <Text strong>{title}</Text>
    </Space>
);