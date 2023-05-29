import { BellOutlined, CodeOutlined, ControlOutlined, FundOutlined, SettingOutlined } from '@ant-design/icons';
import { Layout, Menu, Space, theme, Typography, Table, ConfigProvider } from 'antd';
import React, { useState, useEffect } from 'react';
import '../App.css';
import axios from 'axios';
import { UsageLiquid } from '../Components/UsageLiquid';
import { TemperatureBullet } from '../Components/TemperatureBullet';

const { Content, Sider } = Layout;
const { Text, Title } = Typography;

export const Stats = () => {
    let color_theme = "light";
    const [cpuUsage, SetCpuUsage] = useState(0);
    const [ramUsage, SetRamUsage] = useState(0);
    const [sdUsage, SetSdUsage] = useState(0);
    const [cpuTemperature, SetCpuTemperature] = useState(0);
    const API_URL = "http://localhost:8000"; // FIXIT

    const setStats = () => {
        axios({ method: "GET", url: `${API_URL}/stats` }).then((response) => {
            SetCpuUsage(response.data.cpu_usage);
            SetRamUsage(response.data.ram_usage);
            SetSdUsage(response.data.sd_usage);
            SetCpuTemperature(response.data.cpu_temperature);
        }).catch((response) => {
            console.error("Can't get data");
        });
    }

    useEffect(() => { setStats() }, [])
    const RpiTableData = [
        {
            key: 'local_ip',
            item: 'Local IP',
            value: '192.168.115.200'
        },
        {
            key: 'auth_data',
            item: 'Auth data',
            value: 'pi:pi'
        },
        {
            key: 'gl_git',
            item: 'High-Level git hash',
            value: '97b24441c6ae86d189d4cba92cadcaf976676cfe'
        },
        {
            key: 'ros_status',
            item: 'ROS reports',
            value: 'roscore up; noetic 1.15.14'
        },
        {
            key: 'll_connection',
            item: 'Low-Level SPI connection',
            value: 'Healthy (init packet control sum based check)'
        },

    ];

    const RpiTableColumns = [
        {
            title: 'Item',
            dataIndex: 'item',
            key: 'item',
            render: (_, record) => (
                <Text strong>{record.item}</Text>
            )
        },
        {
            title: 'Value',
            dataIndex: 'value',
            key: 'value',
        },
    ];


    return (
        <>
            <Title level={3}>RPi Statistic</Title>
            <Space direction='horizontal' size='large' style={{ width: '100%', justifyContent: 'center', marginBottom: 40 }}>
                <UsageLiquid percent={cpuUsage} color={"#8BC34A"} title={"CPU"} theme={color_theme} />
                <UsageLiquid percent={ramUsage} color={"#4ac387"} title={"RAM"} theme={color_theme} />
                <UsageLiquid percent={sdUsage} color={"#c34a4a"} title={"SD"} theme={color_theme} />
            </Space>
            <Text strong>CPU temperature</Text>
            <TemperatureBullet current={cpuTemperature} />
            <Table dataSource={RpiTableData} columns={RpiTableColumns} />
        </>
    );
};