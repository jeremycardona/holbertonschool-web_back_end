export default function iterateThroughObject(reportWithIterator) {
  const iterator = reportWithIterator[Symbol.iterator]();
  let result = '';

  for (const employee of iterator) {
    result += `${employee} | `;
  }

  // Remove the trailing ' | ' from the result
  if (result.length > 0) {
    result = result.slice(0, -3); // Remove the last ' | '
  }

  return result;
}
