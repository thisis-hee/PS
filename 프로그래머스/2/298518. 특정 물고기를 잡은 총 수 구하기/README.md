# [level 2] 특정 물고기를 잡은 총 수 구하기 - 298518 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/298518) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > SELECT

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 01월 01일 20:26:08

### 문제 설명

<p>낚시앱에서 사용하는 <code>FISH_INFO</code> 테이블은 잡은 물고기들의 정보를 담고 있습니다. <code>FISH_INFO</code> 테이블의 구조는 다음과 같으며 <code>ID</code>, <code>FISH_TYPE</code>, <code>LENGTH</code>, <code>TIME</code>은 각각 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜를 나타냅니다. </p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>FISH_TYPE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>LENGTH</td>
<td>FLOAT</td>
<td>TRUE</td>
</tr>
<tr>
<td>TIME</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>단, 잡은 물고기의 길이가 10cm 이하일 경우에는 <code>LENGTH</code> 가 NULL 이며, <code>LENGTH</code> 에 NULL 만 있는 경우는 없습니다.</p>

<p><code>FISH_NAME_INFO</code> 테이블은 물고기의 이름에 대한 정보를 담고 있습니다. <code>FISH_NAME_INFO</code> 테이블의 구조는 다음과 같으며, <code>FISH_TYPE</code>, <code>FISH_NAME</code> 은 각각 물고기의 종류(숫자), 물고기의 이름(문자) 입니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>FISH_TYPE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>| FISH_NAME | VARCHAR | FALSE |</p>

<hr>

<h5>문제</h5>

<p><code>FISH_INFO</code> 테이블에서 잡은 <code>BASS</code>와 <code>SNAPPER</code>의 수를 출력하는 SQL 문을 작성해주세요. </p>

<p>컬럼명은 'FISH_COUNT`로 해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>FISH_INFO</code> 테이블이 다음과 같고</p>

<p>ID <br>
|  FISH_TYPE | LENGTH | TIME |<br>
| -- | -- | -- | -- |<br>
| 0 | 0 | 30 | 2021/12/04 |<br>
| 1 | 0 | 50 | 2020/03/07 |<br>
| 2 | 0 | 40 | 2020/03/07 |<br>
| 3 | 1 | 20 | 2022/03/09 |<br>
| 4 | 1 | NULL | 2022/04/08 |<br>
| 5 | 2 | 13 | 2021/04/28 |<br>
| 6 | 0 | 60 | 2021/07/27 |<br>
| 7 | 0 | 55 | 2021/01/18 |<br>
| 8 | 2 | 73 | 2020/01/28 |<br>
| 9 | 2 | 73 | 2021/04/08 |<br>
| 10 | 2 | 22 | 2020/06/28 |<br>
| 11 | 2 | 17 | 2022/12/23 |</p>

<p><code>FISH_NAME_INFO</code>  테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>FISH_TYPE</th>
<th>FISH_NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>BASS</td>
</tr>
<tr>
<td>1</td>
<td>SNAPPER</td>
</tr>
<tr>
<td>2</td>
<td>ANCHOVY</td>
</tr>
</tbody>
      </table>
<p>'BASS' 는 물고기 종류 0에 해당하고, 'SNAPPER' 는 물고기 종류 1에 해당하므로 잡은 'BASS' 와 'SNAPPER' 수는 7마리입니다.</p>
<table class="table">
        <thead><tr>
<th>FISH_COUNT</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges