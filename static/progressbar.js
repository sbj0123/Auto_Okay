const audioPlayer = document.getElementById('audio-player');
const progressBar = document.getElementById('progress-bar');

// 재생 시간에 따라 막대의 너비를 조정합니다.
audioPlayer.addEventListener('timeupdate', function() {
    const duration = audioPlayer.duration; // 전체 재생 시간
    const currentTime = audioPlayer.currentTime; // 현재 재생 시간

    const progress = (currentTime / duration) * 100; // 현재 재생 시간의 백분율
    progressBar.style.width = `${progress}%`; // 막대의 너비를 조정합니다.
})
