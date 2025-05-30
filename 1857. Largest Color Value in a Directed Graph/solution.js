/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function(colors, edges) {
    const n = colors.length;
    const adj = Array.from({ length: n }, () => []);
    const indegree = Array(n).fill(0);

    for (const [u, v] of edges) {
        adj[u].push(v);
        indegree[v]++;
    }

    const dp = Array.from({ length: n }, () => Array(26).fill(0));
    const queue = [];

    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) queue.push(i);
        dp[i][colors.charCodeAt(i) - 97] = 1;
    }

    let visited = 0;
    let maxColor = 0;

    while (queue.length) {
        const node = queue.shift();
        visited++;

        for (const neighbor of adj[node]) {
            for (let c = 0; c < 26; c++) {
                const inc = (colors.charCodeAt(neighbor) - 97 === c) ? 1 : 0;
                dp[neighbor][c] = Math.max(dp[neighbor][c], dp[node][c] + inc);
            }

            indegree[neighbor]--;
            if (indegree[neighbor] === 0) queue.push(neighbor);
        }

        maxColor = Math.max(maxColor, Math.max(...dp[node]));
    }

    return visited === n ? maxColor : -1;
};
