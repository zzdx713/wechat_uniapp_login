// utils/request.js
const BASE_URL = 'https://erp.ciosz.com'; // 替换为你的 Odoo 地址

export function post(url, data) {
    return new Promise((resolve, reject) => {
        uni.request({
            url: `${BASE_URL}${url}`,
            method: 'POST',
            header: {
                'content-type': 'application/json'
            },
            data,
            success(res) {
                if (res.statusCode === 200 && res.data.code === 200) {
                    resolve(res.data);
                } else {
                    uni.showToast({ title: '请求失败', icon: 'none' });
                    reject(res.data.msg || '网络异常');
                }
            },
            fail(err) {
                reject('网络错误');
            }
        });
    });
}