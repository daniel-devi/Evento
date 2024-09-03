const getObjectValues = (list: [object]) => {
    return list.map(object => Object.values(object)).flat();
  };

export default getObjectValues;